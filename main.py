def create_flow(service_spec, deployment_spec, flow_uuid):
    return {
        "deployment_spec": deployment_spec,
        "config_map": "{}"
    }

def delete_flow(config_map, flow_uuid):
    return None
