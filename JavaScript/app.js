const user = {
  name: "Art",
  lastname: "123",
  age: 20,
  nickname: "Genexis",
  hobby: ["run","code","eat"],
  address: {
    street: "123 stringify",
    city: "Berlin",
  },
  married: false,
  greet(){
    return "Hello"
  }
}

const friends = [
  {"name": "Yoan", "nickname": "Yoan123"},
  {"name": "Jane", "nickname": "Jane123"},
  {"name": "John", "nickname": "John123"},
  {"name": "Mary", "nickname": "Mary123"},
  {"name": "Nancy", "nickname": "Nancy123"},
]

user.friends = friends

console.log(JSON.stringify(user)) 