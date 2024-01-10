#!/usr/bin/python3
"""
    101-lazy_matrix_mul Module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
        Multiplies 2 matrices

        Args:
            m_a: first matrix
            m_b: second matrix

        Returns:
            the product of the two matrices
    """
    return numpy.matmul(m_a, m_b)
