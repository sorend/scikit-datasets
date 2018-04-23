"""
LIBSVM E2006-log1p dataset.

@author: David Diaz Vico
@license: MIT
"""

from ..base import load_train_scale


def load_e2006_log1p(return_X_y=False):
    """Load E2006-log1p dataset.

    Loads the E2006-log1p dataset.

    Parameters
    ----------
    return_X_y: bool, default=False
                If True, returns (data, target) instead of a Bunch object..

    Returns
    -------
    data: Bunch
          Dictionary-like object with all the data and metadata.
    (X, y), (X_test, y_test): lists of arrays
                              If return_X_y is True

    """
    return load_train_scale('E2006-log1p',
                            'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/log1p.E2006.train.bz2',
                            'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/log1p.E2006.test.bz2',
                            return_X_y=return_X_y)
