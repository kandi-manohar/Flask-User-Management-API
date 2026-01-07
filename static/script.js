async function addUser() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    await fetch("/users", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({name, email})
    });

    loadUsers();
}

async function loadUsers() {
    const res = await fetch("/users");
    const users = await res.json();
    document.getElementById("users").innerHTML =
        users.map(u => `<li>${u[0]} - ${u[1]}</li>`).join("");
}

loadUsers();
