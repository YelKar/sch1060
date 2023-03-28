window.addEventListener("pointerdown", e => {
    let ctx = document.querySelector(".ctxMenu");
    if (ctx) {
        ctx.remove()
    }
})


function contextMenu(els, event, nodeClass) {
    if (
        nodeClass != undefined
        && !(event.target.classList.contains(nodeClass))
    ) {
        return
    }
    event.preventDefault()
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

    menuStyle.left = `${event.x}px`;
    menuStyle.top = `${event.y}px`;
    for (let [k, v] of Object.entries(els)) {
        let elem = contextEl(k);
        elem.addEventListener("click", function (e) {
            v(event.target);
            menu.remove()
        })
        main.appendChild(elem)
    }
    document.body.append(menu)
    menu.addEventListener("pointerdown", e => {
        e.stopPropagation()
    })
}


function contextEl(text) {
    let el = document.createElement("button")

    el.classList = "container"
    el.textContent = text;

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
