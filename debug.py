import jmespaths

expression = '[?key==`key1`].value'
data = [{'key': 'key1', 'value': 1}]
expression = '[0]'
data = 'fuck you nvidia'.split(' ')
expression='a.b.c[0].d[1][0]'
data={"a": {
  "b": {
    "c": [
      {"d": [0, [1, 2]]},
      {"d": [3, 4]}
    ]
  }
}}
expression="myarray[?contains(@, 'foo') == `true`]"
data={
  "myarray": [
    "foo",
    "foobar",
    "barfoo",
    "bar",
    "baz",
    "barbaz",
    "barfoobaz"
  ]
}
print(jmespaths.replace(expression, data,'fuck'))
print(data)
