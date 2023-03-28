function ctxMenuElsDec(f) {
    async function dec(target) {
        let st = target.htmlFor;
        if (st === undefined) {
            return;
        }
        return await f(Number.parseInt(st.slice(1)))
    }
    return dec
}

let ctxMenuEls = {
    "Удалить": delete_students,
    "Изменить": edit_student
}

for (let [el, f] of Object.entries(ctxMenuEls)) {
    ctxMenuEls[el] = ctxMenuElsDec(f)
}


window.addEventListener("contextmenu", e => {
    contextMenu(ctxMenuEls, e, "student_checkbox_label")
})

async function edit_student(student_id) {
    goto(
        await url_for(
            "edit_student", {student_id:student_id}
        )
    )
}

async function delete_students(ids) {
    if (ids === undefined) {
        ids = get_selected()
    } else if (ids.constructor == Number) {
        ids = [ids]
    }
    if (
        !ids.length ||
        !confirm(
            "Вы точно хотите удалить этих учеников из базы данных?\n"+
            "Восстановить можно будет, только заново записав их в базу данных!"
        )
    ) {
        return
    }
    await fetch(
        document.querySelector("input[type=hidden].delete_link").value,
        {
            method: "POST",
            body: ids.toString()
        }
    );
    ids.forEach((x) => {
        let st = document.querySelector(`*:has(> #s${x})`)
        st.remove()
    })
}
