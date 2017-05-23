ILLEGAL_ARGUMENT = {
    'error_type': "java.lang.IllegalArgumentException",
    'status': 400
}

ROOT_URL_OK = {
    "request": {
        "type": "version"
    },
    "value": {
        "agent": "1.3.6",
        "protocol": "7.2",
        "config": {
            "maxCollectionSize": "0",
            "agentId": "10.195.20.189-18288-6b59e8eb-servlet",
            "debug": "false",
            "agentType": "servlet",
            "serializeException": "false",
            "detectorOptions": "{}",
            "dispatcherClasses": "org.jolokia.jsr160.Jsr160RequestDispatcher",
            "maxDepth": "15",
            "discoveryEnabled": "false",
            "canonicalNaming": "true",
            "historyMaxEntries": "10",
            "includeStackTrace": "true",
            "maxObjects": "0",
            "debugMaxEntries": "100"
        },
        "info": {
            "product": "JBoss EAP",
            "vendor": "RedHat",
            "version": "7.0.0.GA"
        }
    },
    "timestamp": 1494275547,
    "status": 200
}

VALID_GET_HEAP_MEMORY_USAGE = {
    "request": {
        "path": "used",
        "mbean": "java.lang:type=Memory",
        "attribute": "HeapMemoryUsage",
        "type": "read"
    },
    "value": 321815952,
    "timestamp": 1494560184,
    "status": 200
}

VALID_BULK_RESPONSE = [
    {
        "request": {
            "path": "used",
            "mbean": "java.lang:type=Memory",
            "attribute": "HeapMemoryUsage",
            "type": "read"
        },
        "value": 75977776,
        "timestamp": 1495078549,
        "status": 200
    },
    {
        "request": {
            "path": "used",
            "mbean": "java.lang:type=Memory",
            "attribute": "NonHeapMemoryUsage",
            "type": "read"
        },
        "value": 80981104,
        "timestamp": 1495078549,
        "status": 200
    }
]

VALID_WRITE_CLASSLOADING_RESPONSE = {
    "request": {
        "mbean": "java.lang:type=ClassLoading",
        "attribute": "Verbose",
        "type": "write",
        "value": True
    },
    "value": False,
    "timestamp": 1495480324,
    "status": 200
}


def _mock_base(resp_data, status_code, ok, *args, **kwargs):

    import json
    from requests import Response
    resp_json = json.dumps(resp_data)

    resp = Response()
    setattr(Response, 'content', resp_json.encode('utf-8'))
    resp.status_code = status_code
    setattr(Response, 'ok', ok)

    return resp


def mock_request(self, url=None, method=None, data=None, *args, **kwargs):
    pass


# FIXME These need to be DRY
def mock_illegal_arg(self, *args, **kwargs):

    resp = _mock_base(ILLEGAL_ARGUMENT, 400, False)

    return resp.json()


def mock_root_ok(*args, **kwargs):

    resp = _mock_base(ROOT_URL_OK, 200, True)

    return resp.json()


def mock_empty_body(*args, **kwargs):

    resp = _mock_base(ILLEGAL_ARGUMENT, 400, False)

    return resp.json()


def mock_valid_body(*args, **kwargs):

    resp = _mock_base(VALID_GET_HEAP_MEMORY_USAGE, 200, True)

    return resp.json()


def mock_write_valid(*args, **kwargs):

    resp = _mock_base(VALID_WRITE_CLASSLOADING_RESPONSE, 200, True)

    return resp.json()


def mock_get_heap_memory_usage(*args, **kwargs):

    resp = _mock_base(VALID_GET_HEAP_MEMORY_USAGE, 200, True)

    return resp.json()


def mock_bulk_request(*args, **kwargs):

    resp = _mock_base(VALID_BULK_RESPONSE, 200, True)

    return resp.json()