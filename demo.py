from proj import tasks
from proj.transform import Reverse, Capitalize, RaiseException

#tasks.task.delay('foobar')
print(tasks.task(Reverse('foobar')))
tasks.task.delay('foobar')
tasks.task.delay(Reverse('foobar'))
tasks.task.delay(RaiseException())


#tasks.task.delay('capitalize', 'foobar')
