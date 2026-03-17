const API = "http://127.0.0.1:5000";
const USER = "darshan";

async function searchFood(){
    let q = document.getElementById("searchInput").value;

    let res = await fetch(API+"/recommend", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({user:USER, query:q})
    });

    let data = await res.json();
    showFoods(data);
}

async function moodFood(mood){
    let res = await fetch(API+"/mood", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({user:USER, mood:mood})
    });

    let data = await res.json();

    let container = document.getElementById("results");
    container.innerHTML = `
        <h3>${data.quote}</h3>
        <p>🎟 Coupon: ${data.coupon}</p>
    `;

    showFoods(data.foods);
}

async function chatAI(){
    let msg = document.getElementById("chatInput").value;

    let res = await fetch(API+"/chat", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({user:USER, message:msg})
    });

    let data = await res.json();
    alert(data.reply);
}

async function orderFood(name){
    await fetch(API+"/order", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({user:USER, food:name})
    });
}

async function getHistory(){
    let res = await fetch(API+"/history", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({user:USER})
    });

    let data = await res.json();

    let container = document.getElementById("results");
    container.innerHTML = "<h3>Order History</h3>";

    data.forEach(f => {
        container.innerHTML += `<p>${f}</p>`;
    });
}

function showFoods(list){
    let container = document.getElementById("results");

    list.forEach(f => {
        let div = document.createElement("div");
        div.className = "card";

        div.innerHTML = `
            <h3>${f.name}</h3>
            <p>${f.desc}</p>
            <button onclick="orderFood('${f.name}')">Order</button>
        `;

        container.appendChild(div);
    });
}