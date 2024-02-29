import random
import simulation_servers

def random_simulation():

    max_client = random.randint(1, 10)
    min_client = random.randint(1, max_client)
    max_server = random.randint(5, 20)
    min_server = random.randint(1, max_server)
    initial_clients = random.randint(0, 10)
    servers = random.randint(1, 10)
    G_distribution = random.choice(['uniform', 'normal', 'exponential', 'poisson']) 
    Gi_distribution = [ random.choice(['uniform', 'normal', 'exponential', 'poisson']) for i in range (servers) ] 
    M_distribution = random.choice(['uniform', 'normal', 'exponential', 'poisson']) 
    duracion = random.randint(5, 10) 

    simulation_servers.run_simulation(max_client,min_client,max_server,min_server,initial_clients,servers,G_distribution,Gi_distribution,M_distribution,duracion)

if __name__ == "__main__":
    for i in range(100):
        random_simulation()
