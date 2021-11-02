let users = [
    { username: 'user1', password: 'password1' },
    { username: 'user2', password: 'password2' },
    { username: 'user3', password: 'password3' },
    { username: 'user4', password: 'password4' },
    { username: 'user5', password: 'password5' },
    { username: 'user6', password: 'password6' },
    { username: 'user7', password: 'password7' },
    { username: 'user8', password: 'password8' },
]
localStorage.setItem('users', JSON.stringify(users));


function login() {
    let username = document.getElementById('username');
    let password = document.getElementById('password');
    let local_storage_users = localStorage.getItem('users');
    let u = JSON.parse(local_storage_users);
    for (let i = 0; i < u.length; i++) {
        if (
            (u[i].username === username.value) &&
            (u[i].password === password.value)) {
            localStorage.setItem('is_authorized', true);
            window.location.reload();
            return true;
        }
    }
}
function register() {
    let username = document.getElementById('username');
    let password = document.getElementById('password');
    if ((username.value.length > 1) && (password.value.length > 1)) {
        console.log('data is ok');
    } else {
        console.log('invalid data');
    }
    let local_storage_users = JSON.parse(localStorage.getItem('users'));
    console.log(local_storage_users);

    local_storage_users.push({ 'username': username.value, 'password': password.value })
    local_storage_users_json = JSON.stringify(local_storage_users);
    localStorage.setItem('users', local_storage_users_json);
}
function data_edit(){
    var elem_name_data = document.getElementById("name_data").value;
    var A1_id = document.getElementById("A1");
    var elem_country_data = document.getElementById("country_data").value;
    var A2_id = document.getElementById("A2");
    A1_id.innerHTML = elem_name_data; 
    A2_id.innerHTML = elem_country_data; 
}