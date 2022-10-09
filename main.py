import calculator as calc
import gui
from cli import Configuration

def main():
    """ Main function of the program """

    cli = Configuration()
    cli.cmdloop()
    app = gui.MainApplication(cli.einstein, cli.curie, cli.newton, 
                              cli.brigadeiro, cli.pedro, cli.isa)
    app.mainloop()

if __name__ == '__main__':
    main()
