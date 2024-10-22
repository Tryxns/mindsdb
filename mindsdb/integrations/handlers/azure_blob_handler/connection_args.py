from collections import OrderedDict

from mindsdb.integrations.libs.const import HANDLER_CONNECTION_ARG_TYPE as ARG_TYPE


connection_args = OrderedDict(
    storage_account_name={
        'type': ARG_TYPE.STR,
        'description': 'The name of your storage account',
        'required': True,
        'label': 'Storage Account Name'
    },
    account_access_key={
        'type': ARG_TYPE.STR,
        'description': 'Account Access Key',
        'required': True,
        'label': 'Account Access Key'
    },
    container_name={
        'type': ARG_TYPE.STR,
        'description': 'Container Name',
        'required': True,
        'label': 'Container Name'
    }
)

connection_args_example = OrderedDict(
    storage_account_name='',
    account_access_key='',
    container_name=''
)
