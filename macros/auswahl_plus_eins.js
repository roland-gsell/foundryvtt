main()

async function main() {
    console.log("Selection heal macro started")
    let t = canvas.tokens.controlled;
    t.forEach(increase);
}

async function increase(tok){
    let wound = tok.actor.data.data.status.wounds.value;
    let newhit = wound + 1;
    if (newhit > tok.actor.data.data.status.wounds.max){
        newhit = tok.actor.data.data.status.wounds.max
    }
    tok.actor.update({"data.status.wounds.value": newhit});
    console.log("Token: ", tok.actor.name, " before: ", wound, " after: ", newhit)
}
