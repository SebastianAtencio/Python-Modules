import sys
import importlib
import pandas as pd  # type: ignore
import numpy as np
import matplotlib.pyplot as plt  # type: ignore


def check_dependencies() -> dict[str, str]:
    packages = ["pandas", "numpy", "matplotlib"]
    missing = []
    versions: dict[str, str] = {}
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    for lib in packages:
        try:
            pkg = importlib.import_module(lib)
            version = getattr(pkg, "__version__", "unknown")
            versions[lib] = version
            print(f"[OK] {lib} ({version}) - Ready")
        except ImportError:
            missing.append(lib)
            print(f"[MISSING] {lib}")
    if missing:
        print("ERROR: Dependencies missing!")
        print("-" * 30)
        print("To install with pip:")
        print("pip install -r requirements.txt")
        print("To install with Poetry:")
        print("poetry install")
        print("-" * 30)
        sys.exit(1)
    return versions


def run_analysis() -> None:
    print("Analyzing Matrix data: Income Distribution...")
    data_points = 1000
    # 1. Generamos datos con Distribución Normal (Campana)
    incomes = np.random.normal(loc=30000, scale=5000, size=data_points)
    # 2. Pasamos a Pandas para cumplir con el requisito de manipulación
    df = pd.DataFrame(incomes, columns=['Salary'])
    # Manipulación: Calculamos la media y marcamos quién está por encima
    mean_salary = float(df['Salary'].mean())
    df['Status'] = np.where(
        df['Salary'] >= mean_salary, 'Above Average', 'Below Average')
    # 3. Visualización: Histograma con Campana de Gauss
    plt.figure(figsize=(10, 6))
    # Dibujamos el histograma (las barras)
    count, bins, ignored = plt.hist(
        df['Salary'], bins=30, density=True,
        alpha=0.6, color='skyblue', edgecolor='white', label='Ingresos')
    # 4. Dibujamos la línea de la Campana de Gauss teórica
    sigma = float(df['Salary'].std())
    mu = float(df['Salary'].mean())
    gauss_curve = (
        1 / (sigma * np.sqrt(2 * np.pi)) *
        np.exp(- (bins - mu)**2 / (2 * sigma**2))
    )
    plt.plot(bins, gauss_curve, linewidth=3, color='navy', label='Normal')
    # Línea vertical para la media
    plt.axvline(
        mean_salary, color='red', linestyle='--',
        label=f'Media: {mean_salary:.2f}€')
    # Estética
    plt.title('Analisis Ingresos Anuales')
    plt.xlabel('Ingresos anuales (€)')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)

    # Guardar
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    print("Generating statistical visualization...")
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def show_comparison() -> None:
    print("\n[Package Management Comparison]")
    print("Pip: Uses requirements.txt (Static list, manual management)")
    print("Poetry: Uses pyproject.toml (Deterministic, "
          "handles dependencies & build)")


if __name__ == "__main__":
    check_dependencies()
    run_analysis()
    show_comparison()
