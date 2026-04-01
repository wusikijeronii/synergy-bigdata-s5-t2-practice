#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Product:
    name: str
    quantity: int
    material_cost: float
    assembly_time: int
    defect_rate: float

@dataclass
class Order:
    product_name: str
    quantity: int

def process_orders(products: Dict[str, Product], orders: List[Order]) -> None:
    total_material_cost = 0.0
    total_assembly_time = 0
    total_units_produced = 0
    total_defective_units = 0

    print("Warehouse simulation")
    print("=" * 40)

    for order in orders:
        product = products.get(order.product_name)

        if product is None:
            print(f"Order skipped: product '{order.product_name}' not found.")
            continue

        if order.quantity > product.quantity:
            print(
                f"Order skipped: not enough stock for '{product.name}'. "
                f"Available: {product.quantity}, requested: {order.quantity}."
            )
            continue

        produced_units = order.quantity
        defective_units = int(produced_units * product.defect_rate)
        valid_units = produced_units - defective_units

        material_cost = produced_units * product.material_cost
        assembly_time = produced_units * product.assembly_time

        product.quantity -= produced_units

        total_material_cost += material_cost
        total_assembly_time += assembly_time
        total_units_produced += produced_units
        total_defective_units += defective_units

        print(f"Processed order: {product.name}")
        print(f"  Produced units: {produced_units}")
        print(f"  Defective units: {defective_units}")
        print(f"  Valid units: {valid_units}")
        print(f"  Material cost: {material_cost:.2f}")
        print(f"  Assembly time: {assembly_time} min")
        print(f"  Remaining stock: {product.quantity}")
        print()

    workers = 3
    workday_minutes = 8 * 60
    total_available_minutes = workers * workday_minutes

    print("=" * 40)
    print("Summary:")
    print(f"Total produced units: {total_units_produced}")
    print(f"Total defective units: {total_defective_units}")
    print(f"Total material cost: {total_material_cost:.2f}")
    print(f"Total assembly time: {total_assembly_time} min")

    if total_assembly_time <= total_available_minutes:
        print("Recommended staff schedule: current staff is sufficient.")
    else:
        extra_days = (total_assembly_time + total_available_minutes - 1) // total_available_minutes
        print(
            "Recommended staff schedule: additional working time is required. "
            f"Estimated duration: {extra_days} workday(s)."
        )

def main() -> None:
    products = {
        "Widget A": Product("Widget A", 50, 10.0, 15, 0.05),
        "Widget B": Product("Widget B", 30, 18.0, 25, 0.08),
        "Widget C": Product("Widget C", 20, 25.0, 35, 0.10),
    }

    orders = [
        Order("Widget A", 10),
        Order("Widget B", 8),
        Order("Widget C", 5),
        Order("Widget A", 15),
    ]

    process_orders(products, orders)

if __name__ == "__main__":
    main()