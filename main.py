from service.arquivosService import engine, Base
from view.app import App

Base.metadata.create_all(bind=engine)
app = App()
app.mainloop()

