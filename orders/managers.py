from django.db.models.query import QuerySet


class OrderQuerySet(QuerySet):
    def orders(self):
        pass
