from duwin_backend.serializers import BaseSerializer

from django.apps import apps


serializers = {
    f"{i.__name__}":
        type(
            f"{i.__name__}Serializer",
            (BaseSerializer, ),
            {
                "Meta": type("Meta", (), {
                    "model": i,
                    "fields": "__all__"
                })
            }
        ) for i in apps.get_app_config("core").get_models()
}


