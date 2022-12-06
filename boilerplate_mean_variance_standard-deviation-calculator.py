import numpy as np

testlist = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def calculate(list):
    if len(list) == 9:
        nparr = np.array(list).reshape(3, 3)

        mean = [nparr.mean(axis=0).tolist(), nparr.mean(
            axis=1).tolist(), np.array(list).mean().tolist()]

        variance = [nparr.var(axis=0).tolist(), nparr.var(
            axis=1).tolist(), np.array(list).var().tolist()]

        std = [nparr.std(axis=0).tolist(), nparr.std(
            axis=1).tolist(), np.array(list).std().tolist()]

        max = [nparr.max(axis=0).tolist(), nparr.max(
            axis=1).tolist(), np.array(list).max().tolist()]

        min = [nparr.min(axis=0).tolist(), nparr.min(
            axis=1).tolist(), np.array(list).min().tolist()]

        sum = [nparr.sum(axis=0).tolist(), nparr.sum(
            axis=1).tolist(), np.array(list).sum().tolist()]

        calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': std,
            'max': max,
            'min': min,
            'sum': sum
        }
        return calculations
    else:
        raise ValueError('List must contain nine numbers.')


print(calculate([0, 1, 2, 3, 4, 5, 6]))
