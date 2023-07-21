class BaseDBRouter:
    route_app_labels = None
    db_name = None

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class AuthRouter(BaseDBRouter):
    route_app_labels = {'auth', 'admin', 'contenttypes', 'sessions'}
    db_name = 'auth_db'


class StoreRouter(BaseDBRouter):
    route_app_labels = {'store'}
    db_name = 'store_db'


class WarehouseRouter(BaseDBRouter):
    route_app_labels = {'warehouse'}
    db_name = 'warehouse_db'
