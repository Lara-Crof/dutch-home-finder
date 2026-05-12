class HouseMessageFormatter:
    @staticmethod
    def price(v: int) -> str:
        return f"€{v:,}".replace(",", " ")

    @staticmethod
    def optional(v, default="N/A") -> str:
        return v if v else default

    @staticmethod
    def date(v) -> str:
        return v.strftime("%Y-%m-%d") if v else "N/A"

    @staticmethod
    def area(v) -> str:
        return f"{v} m²"