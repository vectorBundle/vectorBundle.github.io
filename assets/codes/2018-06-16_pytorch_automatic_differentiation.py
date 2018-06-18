'''
This script illustrates automatic differentiation using PyTorch.
'''


# define the EOS with constants filled in
def pressure(T, v):
    return 8.314 * T / (v - 8.09e-5) - 29.08 / (T**(0.5) * v * (v + 8.09e-5))


# we can leverage numpy to evaluate the function
import numpy as np
T = np.arange(25 + 273.15, 100 + 273.15, 15)
v = np.linspace(1.27e-3, 2.59e-3, T.shape[0])
np_pres = pressure(T, v)
print(np_pres)

# we can use PyTorch to evaluate the function as well without change the source
# code
import torch
T = torch.tensor(np.arange(25 + 273.15, 100 + 273.15, 15), requires_grad=True)
v = torch.tensor(np.linspace(1.27e-3, 2.59e-3, T.shape[0]), requires_grad=True)
tc_pres = pressure(T, v)
print(tc_pres)

# check that the calculations are actually identical
print(np.allclose(tc_pres.detach().numpy(), np_pres))

# now compute the first order derivative
dPdT, dPdv = torch.autograd.grad(
    [tc_pres.sum()], [T, v],
    retain_graph=True,
    create_graph=True,
    allow_unused=True)
print("dP/dT:", dPdT)
print("dP/dv:", dPdv)


# compare against symbolic differentiation results
def dP_by_dT(T, v):
    return 8.314 / (v - 8.09e-5) + 29.08 / (2 * T**(3 / 2) * v * (v + 8.09e-5))


def dP_by_dv(T, v):
    numerator = 29.08 * (2 * v + 8.09e-5)
    denominator = T**(1 / 2) * v**2 * (v + 8.09e-5)**2
    return -8.314 * T / (v - 8.09e-5)**2 + numerator / denominator


print(np.allclose(dPdT.detach().numpy(), dP_by_dT(T, v).detach().numpy()))
print(np.allclose(dPdv.detach().numpy(), dP_by_dv(T, v).detach().numpy()))

# compute the second order derivatives
print(
    torch.stack(
        torch.autograd.grad(
            [dPdT.sum()], [T, v],
            retain_graph=True,
            create_graph=True,
            allow_unused=True)))
print(
    torch.stack(
        torch.autograd.grad(
            [dPdv.sum()], [T, v],
            retain_graph=True,
            create_graph=True,
            allow_unused=True)))
