import requests
import webbrowser
from tkinter import messagebox

ENDPOINT = "https://pixe.la/v1/users"
COLOR_DICT = {
    'red': 'momiji',
    'green': 'shibafu',
    'blue': 'sora',
    'yellow': 'ichou',
    'purple': 'ajisai',
    'black': 'kuro'
}


def create_account(password, user_name):
    # Step 1: Create a user:
    user_params = {
        'token': password,
        'username': user_name,
        'agreeTermsOfService': "yes",
        'notMinor': "yes",
    }

    response = requests.post(url=ENDPOINT, json=user_params)
    response_mess = response.json()["message"]
    response_result = response.json()["isSuccess"]

    if not response_result:
        response_result = "Warning."
    else:
        response_result = "Success!"
        response_mess = response_mess.replace("Success. ", "Success.\n")
        webbrowser.open(f"https://pixe.la/@{user_name}")

    messagebox.showinfo(title=response_result, message=response_mess)


def create_graph(user_name, user_token, graph_id, graph_name, unit_name, unit_type, color_pick):
    # Step 2: Create a graph:
    graph_create_endpoint = f"{ENDPOINT}/{user_name}/graphs"
    graph_params = {
        'id': graph_id,
        'name': graph_name,
        'unit': unit_name,
        'type': unit_type,
        'color': COLOR_DICT[color_pick.lower()],
    }

    headers = {
        "X-USER-TOKEN": user_token,
    }

    response_graph = requests.post(url=graph_create_endpoint, json=graph_params, headers=headers)
    check_response(response=response_graph, user_name=user_name, graph_id=graph_id)


def create_value(user_name, user_token, graph_id, d_day, q_quantity):
    # Step 3: update the graph with a value
    graph_update_endpoint = f"{ENDPOINT}/{user_name}/graphs/{graph_id}"

    update_params = {
        'date': d_day,
        'quantity': q_quantity,
    }

    headers = {
        "X-USER-TOKEN": user_token,
    }

    response_update = requests.post(url=graph_update_endpoint, json=update_params, headers=headers)
    check_response(response=response_update, user_name=user_name, graph_id=graph_id)


def check_response(response, user_name, graph_id):
    try:
        response_mess = response.json()["message"]
        response_result = response.json()["isSuccess"]

        if not response_result:
            response_result = "Warning."
        else:
            response_result = "Success!"
            response_mess = f"Success, the data has been processed!\n" \
                            f"Link: {ENDPOINT}/{user_name}/graphs/{graph_id}.html"
            webbrowser.open(f"{ENDPOINT}/{user_name}/graphs/{graph_id}.html")

    except requests.exceptions.JSONDecodeError:
        response_result = "Warning."
        response_mess = "Error, insert valid user name."

    messagebox.showinfo(title=response_result, message=response_mess)
