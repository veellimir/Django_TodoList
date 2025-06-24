class ModelStrMixin:
    def __str__(self) -> str:
        if hasattr(self, 'username') and self.username:
            return f"{self.username}"
        elif hasattr(self, 'name') and self.name:
            return f"{self.name}"
        elif hasattr(self, 'title') and self.title:
            return f"{self.title}"
        return super().__str__()