# Raboof

A proof of concept for how to handle girder_worker input bindings while calling functions with the celery API.  This code does not depend on girder or girder worker. It is a minimum example that displays the functionality in question

## Getting started

Checkout the repository,  

Make sure you have RabbitMQ running locally
```sh
docker run --net=host --rm -d rabbitmq:latest
```

Run celery from the root of the repository
```sh
celery worker -A proj -l info
```

Run demo.py in a different terminal
```
python demo.py
```


## What is happening

The ```proj``` module has one task ```task``` that simply prints out the argument passed to it.

```demo.py``` calls ```task.delay()``` with several arguments:

```python
task.delay('foobar')          # Worker prints out 'foobar'
task.delay(Reverse('foobar')) # Worker prints out 'raboof', the reverse of 'foobar'
task.delay(RaiseException())  # Task transformation raises an exception and moves task into 'fail' state correctly
```

The actual code that implements the string reverse is defined in ```Reverse.transform()``` the ```Reverse``` object is serialized in the producer process (demo.py)  and serialized in the consumer process (celery worker).  Before executing the actual task function consumer-side,  we call ```transform()``` on the Reverse object. The task object recieves 'raboof' rather than 'foobar'

Critically,  the transform function:
+ Is defined producer side at call-time (like a girder input binding).
+ Executed consumer side (i.e. inside the worker process)
+ The function recieves the "right" data regardless of whether the transform is applied producer side or not (e.g.,  passing in 'foobar' still works as expected).

## Compatibility with Item Tasks
It would be relatively easy to convert functions like [girderInputSpec](https://github.com/girder/girder/blob/master/plugins/worker/server/utils.py#L36-L74) to return these objects rather than raw dictionaries. A transform object like ```ItemIdToLocalFilePath``` could ensure that a custom celery task would receive a local file path,  rather than an item ID. 

With slight extension, It should be easy to define custom functions
for more exotic use cases. E.g.:

```python
docker_run.delay('org/docker_container:latest', 
    volume_mounts=[FolderIdToLocalPath(folder['_id']),
                   FolderIdToLocalPath(folder2['_id])])
```

```python
custom_task.delay(FileIdToLocalFilePath(
    file['_id'],  check_path_first=adapter.fullPath(item))
```

```python
custom_task.delay(arg1, arg2,
                  stdin=NamedPipe('stdin'), 
                  stdout=NamedPipe('stdout'))
```
