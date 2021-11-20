#include <Python.h>
#include <cstdio>

#include "graph.hh"

static void _destroy(PyObject *capsule)
{
  bliss::Graph* g = (bliss::Graph*)PyCapsule_GetPointer(capsule, "bliss_graph");
  if(g)
    {
      delete g;
    }
}

static PyObject *
graph_create(PyObject *self, PyObject *args)
{
  bliss::Graph *g = new bliss::Graph();
  if(!g)
    Py_RETURN_NONE;
  
  PyObject *py_g = PyCapsule_New(g, "bliss_graph", &_destroy);
  if(!py_g)
    Py_RETURN_NONE;
  return py_g;
}


static PyObject *
add_vertex(PyObject *self, PyObject *args)
{
  PyObject *py_g = NULL;
  unsigned int color;

  if(!PyArg_ParseTuple(args, "OI", &py_g, &color))
    Py_RETURN_NONE;
  if(!PyCapsule_CheckExact(py_g))
    Py_RETURN_NONE;

  bliss::Graph* g = (bliss::Graph *)PyCapsule_GetPointer(py_g, "bliss_graph");
  assert(g);

  unsigned int v = g->add_vertex(color);
  PyObject *py_N = PyLong_FromLong(v);
  if(!py_N)
    Py_RETURN_NONE;
  return py_N;
}


static PyObject *
add_edge(PyObject *self, PyObject *args)
{
  PyObject *py_g = NULL;
  unsigned int v1;
  unsigned int v2;

  if(!PyArg_ParseTuple(args, "OII", &py_g, &v1, &v2))
    Py_RETURN_NONE;
  if(!PyCapsule_CheckExact(py_g))
    Py_RETURN_NONE;

  bliss::Graph* g = (bliss::Graph *)PyCapsule_GetPointer(py_g, "bliss_graph");
  assert(g);

  g->add_edge(v1, v2);
  Py_RETURN_NONE;
}


typedef struct {
  PyObject *py_reporter;
  PyObject *py_reporter_arg;
} ReporterStruct;


static void
_reporter(void *user_param,
	  const unsigned int N,
	  const unsigned int *aut)
{
  if(!user_param)
    return;
  ReporterStruct *s = (ReporterStruct *)user_param;
  /*PyObject *py_reporter = (PyObject*)user_param;*/
  if(!s->py_reporter)
    return;

  PyObject* py_aut = PyList_New(N);
  if(!py_aut)
    {
      return;
    }
  
  for(unsigned int i = 0; i < N; i++)
    if(PyList_SetItem(py_aut, i, PyLong_FromLong((long)aut[i])) != 0)
      return;

  PyObject* args = PyTuple_Pack(2, py_aut, s->py_reporter_arg);
  PyObject* result = PyObject_Call(s->py_reporter, args, NULL);
  if(result)
    Py_DECREF(result);
  Py_DECREF(args);
  Py_DECREF(py_aut);
}



static PyObject *
pybliss_canonical_form(PyObject *self, PyObject *args)
{
  PyObject *py_g = NULL;
  PyObject *py_reporter = NULL;
  PyObject *py_reporter_arg = NULL;
  bliss::Graph *g = 0;

  if(!PyArg_ParseTuple(args, "OOO", &py_g, &py_reporter, &py_reporter_arg))
    Py_RETURN_NONE;
  if(!PyCapsule_CheckExact(py_g))
    Py_RETURN_NONE;
  if(!PyFunction_Check(py_reporter))
    {
      assert(py_reporter == Py_None);
      py_reporter = NULL;
    }

  g = (bliss::Graph *)PyCapsule_GetPointer(py_g, "bliss_graph");
  assert(g);

  bliss::Stats stats;
  ReporterStruct s;
  s.py_reporter = py_reporter;
  s.py_reporter_arg = py_reporter_arg;
  const unsigned int *cl = g->canonical_form(stats, &_reporter, &s);

  const unsigned int N = g->get_nof_vertices();

  PyObject* py_cl = PyList_New(N);
  if(!py_cl)
    Py_RETURN_NONE;
  
  for(unsigned int i = 0; i < N; i++)
    if(PyList_SetItem(py_cl, i, PyLong_FromLong((long)cl[i])) != 0)
      Py_RETURN_NONE;

  return py_cl;
}


static PyObject *
pybliss_find_automorphisms(PyObject *self, PyObject *args)
{
  PyObject *py_g = NULL;
  PyObject *py_reporter = NULL;
  PyObject *py_reporter_arg = NULL;
  bliss::Graph *g = 0;
  
  if(!PyArg_ParseTuple(args, "OOO", &py_g, &py_reporter, &py_reporter_arg))
    Py_RETURN_NONE;
  if(!PyCapsule_CheckExact(py_g))
    Py_RETURN_NONE;
  if(!PyFunction_Check(py_reporter))
    {
      assert(py_reporter == Py_None);
      py_reporter = NULL;
    }

  
  g = (bliss::Graph *)PyCapsule_GetPointer(py_g, "bliss_graph");
  assert(g);

  bliss::Stats stats;
  ReporterStruct s;
  s.py_reporter = py_reporter;
  s.py_reporter_arg = py_reporter_arg;
  g->find_automorphisms(stats, &_reporter, &s);
  Py_RETURN_NONE;
}


static PyMethodDef Methods[] = {
    {"create",  graph_create, METH_VARARGS, ""},
    /*{"delete",  graph_delete, METH_VARARGS, ""},*/
    /*{"read_dimacs", graph_read_dimacs, METH_VARARGS, ""},*/
    /*{"nof_vertices", nof_vertices, METH_VARARGS, ""},*/
    {"add_vertex", add_vertex, METH_VARARGS, ""},
    {"add_edge", add_edge, METH_VARARGS, ""},
    /*{"write_dot",  pybliss_write_dot, METH_VARARGS,
      "Write the graph into a file in the graphviz dot format."},*/
    {"canonical_form",  pybliss_canonical_form, METH_VARARGS,
     "Transform the graph into canonical form."},
    {"find_automorphisms",  pybliss_find_automorphisms, METH_VARARGS,
     "Find a generating set for Aut(G)."},
    /*{"graph_permute", graph_permute, METH_VARARGS, ""},*/
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


static struct PyModuleDef cModPyDem =
{
    PyModuleDef_HEAD_INIT,
    "intpybliss", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    Methods
};


PyMODINIT_FUNC PyInit_intpybliss(void)
{
  return PyModule_Create(&cModPyDem);
}

