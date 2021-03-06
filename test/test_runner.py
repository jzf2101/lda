from microscopes.lda import model, runner
from microscopes.lda.definition import model_definition
from microscopes.lda.testutil import toy_dataset, permutations
from microscopes.common.rng import rng
from microscopes.common.variadic.dataview import numpy_dataview


import numpy as np


def test_runner_simple():
    N, V = 10, 100
    defn = model_definition(N, V)
    data = toy_dataset(defn)
    view = numpy_dataview(data)
    prng = rng()
    latent = model.initialize(defn, view, prng)
    kc = runner.default_kernel_config(defn)
    r = runner.runner(defn, view, latent, kc)
    r.run(prng, 1)
