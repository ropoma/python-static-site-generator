import typer
import ssg.site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}
    ssg.site.Site(**config).build()


typer.run(main)
