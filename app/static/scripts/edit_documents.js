let docs = document.querySelectorAll("div.document.container")
let contextMenuEls = {
    delete: "Удалить",
    // el: "Элемент",
}

function contextMenu(doc, e) {
    let menu = document.createElement("div")
    let main = document.createElement("div")
    let menuStyle = menu.style
    menu.append(main)
    menu.classList = "container ctxMenu"

    menuStyle.margin = "0";
    menuStyle.width = "auto";
    menuStyle.minWidth = "160px";
    menuStyle.padding = "0";
    menuStyle.display = "block";
    menuStyle.position = "fixed";
    menuStyle.borderRadius = "10px"
    menuStyle.border = "3px solid #111"
    menuStyle.boxSizing = "border-box"
    main.style.margin = "10px"
    menuStyle.backgroundColor = "#222"

    menuStyle.left = `${e.x}px`;
    menuStyle.top = `${e.y}px`;
    for (let el of Object.entries(contextMenuEls)) {
        let elem = contextEl(...el);
        elem.addEventListener("click", e => {
            command(el[0], doc.textContent.trim());
            menu.remove()
        })
        main.appendChild(elem)
    }
    document.body.append(menu)
    menu.addEventListener("pointerdown", e => {
        e.stopPropagation()
    })
}

function contextEl(name, text) {
    let el = document.createElement("button")

    el.classList = "container"
    el.textContent = text;
    el.id = name;
    el.onclick = console.log

    let style = el.style
    style.display = "block";
    style.boxSizing = "border-box";

    style.width = "100%";
    style.margin = "10px 0";
    style.borderRadius = "5px";
    style.border = "3px solid #111"
    style.padding = "3px 10px"
    style.backgroundColor = "#333";
    style.color = "#aaa";
    style.fontWeight = "bold";
    style.fontFamily = "Nunito, sans-serif";

    style.cursor = "pointer";
    return el;
}
document.body.addEventListener("pointerdown", e => {
    let menu = document.querySelector(".ctxMenu")
    if (menu) {
        menu.remove()
    }
})

for (let doc of docs) {
    doc.addEventListener("contextmenu", e => {
        e.preventDefault()
        contextMenu(doc, e);
    })
}
function command(comm, doc) {
    switch (comm) {
        case "delete":
            if (!confirm("Вы точно хотите удалить этот документ?")) {
                return
            }
            break
    }
    let form = new FormData();
    form.append("command", comm);
    form.append("document", doc);
    fetch(
        document.querySelector("input[type=hidden]#link").value,
        {
            method: "POST",
            body: form
        }
    )
    switch (comm) {
        case "delete":
            window.location.reload();
            break
    }
}