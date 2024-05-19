import numpy as np

class Function:
    def __init__(self, func: str) -> None:
        self.func = func
        
    def F(self, coor: np.ndarray) -> float:
        x, y = coor
        return eval(self.func)
    
def det(matrix: np.ndarray) -> float:
    return np.linalg.det(matrix)

def euqlean_metric(point1: np.ndarray, point2: np.ndarray) -> float:
    return np.sqrt(
        np.sum(
            np.square(point1 - point2)
        )
    )

if __name__ == "__main__":
    func1 = Function("x**2 * y**2 - 3*x**2 - 6*y**3 + 8")
    func2 = Function("x**4 - 9*y + 2")
    J = np.array([
        [Function("2*x*y**2 - 6*x"), Function("2*x**2*y - 18*y**2")],
        [Function("4*x**3"), Function("-9")]
    ])
    
    In = 0.0
    I2n = 10.0
    coors = list()
    coors.append(np.array([-17.0, 55.0]))
    Det = det(np.array([
        [J[0][0].F(coors[-1]), J[0][1].F(coors[-1])],
        [J[1][0].F(coors[-1]), J[1][1].F(coors[-1])]
    ]
    ))
    
    coors.append(coors[-1] - np.array([func1.F(coors[-1]), func2.F(coors[-1])]) / Det)
    n=1
    
    print(f"\niter={n},\ninnacurancy={euqlean_metric(coors[-1], coors[-2])},\nanswer={coors[-1]}")
    
    while euqlean_metric(coors[-1], coors[-2]) > 10**(-5):
        Det = det(np.array([
            [J[0][0].F(coors[-1]), J[0][1].F(coors[-1])],
            [J[1][0].F(coors[-1]), J[1][1].F(coors[-1])]
        ]
        ))
        
        coors.append(coors[-1] - np.array([func1.F(coors[-1]), func2.F(coors[-1])]) / Det)
        n += 1
        print(f"\niter={n},\ninnacurancy={euqlean_metric(coors[-1], coors[-2])},\nanswer={coors[-1]}")