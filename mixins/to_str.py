class ModelStrMixin:
    def __str__(self) -> str:
        if hasattr(self, "username") and self.username:
            return f"{self.username}"
        return super().__str__()