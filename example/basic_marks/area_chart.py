import gosling as gos

data = gos.Data(
    url="https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
    type="multivec",
    row="sample",
    column="position",
    value="peak",
    categories=["sample 1"],
)

track = gos.Track(data).mark_area().encode(
    x=gos.Channel("position:G",
        domain=gos.Domain(chromosome="1", interval=[2000500, 3000500]),
        axis="bottom",
    ),
    y="peak:Q",
    size=gos.value(2),
).properties(width=800, height=180, layout="linear")

track.view(title="Basic Marks: Area", subtitle="Tutorial Examples")