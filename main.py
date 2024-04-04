import flask

from safeTravelsBackEnd import safeTravels

safeTravels = safeTravels()

if __name__ == "__main__":

    safeTravels.run(debug = True)
    safeTravels.permanent_session_lifetime=False