main()

async function main() {
    console.log("player AoE macro started")
    let t = canvas.scene.tokens.filter(t => t.actor && t.actor.hasPlayerOwner);
    t.forEach(decrease);
}

async function decrease(tok){
    let wound = tok.actor.data.data.status.wounds.value;
    let newhit = wound - 3;
    if (newhit > tok.actor.data.data.status.wounds.max){
        newhit = tok.actor.data.data.status.wounds.max
    }
    tok.actor.update({"data.status.wounds.value": newhit});
    console.log("Token: ", tok.actor.name, " before: ", wound, " after: ", newhit)
}
