from proj import tasks

tasks.task.delay('reverse', 'foobar')
tasks.task.delay('capitalize', 'foobar')
