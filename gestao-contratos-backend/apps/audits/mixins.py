from .services import get_related_contract, record_audit_event


class AuditedModelViewSetMixin:
    audit_actions = {
        'create': 'CRIACAO',
        'update': 'ATUALIZACAO',
        'delete': 'EXCLUSAO',
    }

    def get_audit_description(self, operation, instance):
        entity_name = str(instance._meta.verbose_name)
        return f'{entity_name} "{instance}" - {operation.lower()} realizada.'

    def perform_create(self, serializer):
        instance = serializer.save()
        record_audit_event(
            request=self.request,
            action=self.audit_actions['create'],
            description=self.get_audit_description('Criacao', instance),
            instance=instance,
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        record_audit_event(
            request=self.request,
            action=self.audit_actions['update'],
            description=self.get_audit_description('Atualizacao', instance),
            instance=instance,
        )

    def perform_destroy(self, instance):
        description = self.get_audit_description('Exclusao', instance)
        contract = get_related_contract(instance, include_contract=False)
        instance.delete()
        record_audit_event(
            request=self.request,
            action=self.audit_actions['delete'],
            description=description,
            contract=contract,
        )
