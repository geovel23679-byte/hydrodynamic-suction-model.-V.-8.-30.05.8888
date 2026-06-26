"""
Hydrodynamic Suction Model
Core module for hydrodynamic simulations and analysis.
"""

import numpy as np
from typing import Dict, Tuple


class SuctionModel:
    """
    Main hydrodynamic suction model class for simulating fluid dynamics behavior.
    
    This model simulates pressure and velocity variations in suction systems
    over time for engineering analysis and research purposes.
    """
    
    def __init__(self, parameters: Dict = None):
        """
        Initialize the suction model with physical parameters.
        
        Args:
            parameters: Dictionary of model parameters. If None, uses defaults.
        """
        self.parameters = parameters or self._default_parameters()
        self.results = None
        
    @staticmethod
    def _default_parameters() -> Dict:
        """Return default physical parameters for the model."""
        return {
            'density': 1000.0,      # kg/m³
            'viscosity': 0.001,     # Pa·s
            'pressure': 101325.0,   # Pa (atmospheric)
            'temperature': 293.15,  # K (20°C)
            'velocity': 1.0,        # m/s
        }
    
    def simulate(self, time_steps: int = 100) -> Dict:
        """
        Run hydrodynamic simulation over time.
        
        Args:
            time_steps: Number of simulation steps (default: 100)
            
        Returns:
            Dictionary containing time, pressure, velocity, and density data.
        """
        time = np.linspace(0, 1, time_steps)
        
        # Calculate pressure variation using sinusoidal oscillation
        pressure_variation = self.parameters['pressure'] * (
            1 + 0.1 * np.sin(2 * np.pi * time)
        )
        
        # Calculate velocity variation using cosine oscillation
        velocity_variation = self.parameters['velocity'] * (
            1 + 0.05 * np.cos(2 * np.pi * time)
        )
        
        self.results = {
            'time': time,
            'pressure': pressure_variation,
            'velocity': velocity_variation,
            'density': self.parameters['density'],
        }
        
        return self.results
    
    def get_results(self) -> Dict:
        """Get simulation results.
        
        Returns:
            Dictionary with simulation results.
            
        Raises:
            ValueError: If no simulation has been run yet.
        """
        if self.results is None:
            raise ValueError("No simulation results. Run simulate() first.")
        return self.results
    
    def plot_results(self):
        """Plot pressure and velocity results.
        
        Requires matplotlib to be installed.
        
        Raises:
            ValueError: If no simulation has been run yet.
            ImportError: If matplotlib is not installed.
        """
        try:
            import matplotlib.pyplot as plt
            
            if self.results is None:
                raise ValueError("No results to plot. Run simulate() first.")
            
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
            
            # Plot pressure
            ax1.plot(self.results['time'], self.results['pressure'], 
                    'b-', linewidth=2, label='Pressure')
            ax1.set_xlabel('Time (s)')
            ax1.set_ylabel('Pressure (Pa)')
            ax1.set_title('Pressure Variation Over Time')
            ax1.grid(True, alpha=0.3)
            ax1.legend()
            
            # Plot velocity
            ax2.plot(self.results['time'], self.results['velocity'], 
                    'r-', linewidth=2, label='Velocity')
            ax2.set_xlabel('Time (s)')
            ax2.set_ylabel('Velocity (m/s)')
            ax2.set_title('Velocity Variation Over Time')
            ax2.grid(True, alpha=0.3)
            ax2.legend()
            
            plt.tight_layout()
            plt.show()
            
        except ImportError:
            print("Matplotlib not installed. Install with: pip install matplotlib")


if __name__ == "__main__":
    # Example usage
    print("Initializing Hydrodynamic Suction Model...")
    model = SuctionModel()
    
    print("Running simulation...")
    results = model.simulate(time_steps=100)
    
    print("Simulation completed successfully!")
    print(f"Results keys: {list(results.keys())}")
    print(f"Max pressure: {results['pressure'].max():.2f} Pa")
    print(f"Min pressure: {results['pressure'].min():.2f} Pa")