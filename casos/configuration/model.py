def define_model_hiperparameters():
    units=56
    epochs=150
    batch_size=16
    adam_opt=0.001

    # Fixing random state for reproducibility
    #np.random.seed(19680801)

    return units, epochs, batch_size, adam_opt
