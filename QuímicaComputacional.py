class GuptaPotential:

    def neb(self, c1, c2, k=1, n=10):
    
        # Cálculo de los estados de transición
        ts = self._neb_transition_states(c1, c2, k=k, n=n)

        # Optimización de las imágenes intermedias
        for i, c in enumerate(ts):
            ts[i] = self.optimize(c)

        # Retorno de la lista de configuraciones
        return ts

    def _neb_transition_states(self, c1, c2, k=1, n=10):

        # Cálculo de la distancia entre las dos configuraciones
        dist = np.linalg.norm(c1 - c2)

        # Creación de las imágenes intermedias
        images = [c1 + (c2 - c1) * i / (n - 1) for i in range(n)]

        # Definición de la matriz de fuerzas
        forces = np.zeros_like(images)

        # Cálculo de las fuerzas iniciales
        forces[0] = self.forces(images[0])
        forces[-1] = self.forces(images[-1])

        # Iteración para encontrar los estados de transición
        for i in range(1, n - 1):
            force_i = self.forces(images[i])

            # Cálculo de la fuerza elástica
            f_elastic = k * (np.linalg.norm(images[i + 1] - images[i]) -
                             np.linalg.norm(images[i] - images[i - 1])) * (images[i + 1] - images[i])
            f_elastic -= k * (np.linalg.norm(images[i] - images[i - 1]) -
                              np.linalg.norm(images[i - 1] - images[i - 2])) * (images[i] - images[i - 1])

            # Cálculo de la fuerza total
            forces[i] = force_i - f_elastic

        # Cálculo de las energías
        energies = np.array([self.potential(image) for image in images])

        # Cálculo de la distancia entre las imágenes
        dists = np.array([np.linalg.norm(images[i + 1] - images[i]) for i in range(n - 1)])
        
        # Definición de la matriz de proyecciones
        projections = dists / dist

        # Definición de la matriz de fuerzas proyectadas
        forces_proj = forces[:-1] * projections.reshape((n - 2, 1)) + forces[1:] * projections[::-1].reshape((n - 2, 1))

        # Cálculo de la fuerza tangencial
        forces_tang = forces_proj - (forces_proj.sum(axis=0) / (n - 2))

        # Cálculo de la fuerza total
        forces_total = np.zeros_like(images)
        forces_total[0] = forces[0]
        forces_total[-1] = forces[-1]
        forces_total[1:-1] = forces_tang

        # Cálculo de los estados de transición
        ts = []
        for i in range(n):
            ts.append(images[i] + forces_total[i] / 2)

        return ts
