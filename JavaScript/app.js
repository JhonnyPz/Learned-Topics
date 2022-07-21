let friendsElements = ""

fetch('/user.json')
 .then(response => response.json())
 .then(data => {
  document.getElementById("userlist").innerHTML = `<h1>${data.name} ${data.lastname}</h1>`
  for (let i = 0; i < data.friends.length; i++){
    friendsElements += `<li>${data.friends[i].name} - ${data.friends[i].nickname}</li>`
  }
  document.getElementById("friendslist").innerHTML = friendsElements
 })

let postsElements = ""

fetch('https://jsonplaceholder.typicode.com/posts')
  .then(res => res.json())
  .then(data => {
    for (let i = 0; i < data.length; i++){
      postsElements += `<li>${data[i].userId} - ${data[i].title}</li>`
    }
    document.getElementById("posts").innerHTML = postsElements
  })