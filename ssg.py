import typer
import ssg.site


def main(source="content", dest="dist"):
    config = {'source': source, 'dest': dest}
    site = ssg.site.Site(**config)
    site.build()


typer.run(main)
