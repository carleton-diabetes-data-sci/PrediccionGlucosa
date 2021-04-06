def crear_grafica_comidasExp(path_comidas_exp):
  comidas_procesadas = pd.read_csv(root+'001'+'/comidas_procesadas.csv')

  eje_x = np.arange(comidas_procesadas.shape[0])
  print(eje_x.shape)

  fig, ax = plt.subplots()
  ax.plot(eje_x, comidas_procesadas['calories_exp'], color='blue', label='Calories')
  plt.title('Patient 1 Calorie absorption')
  plt.xlabel('Time instant (min)')
  plt.ylabel('Calories (cal)')
  leg = ax.legend()


  plt.savefig(path_comidas_exp)

  plt.show()


def crear_grafica_calidad(root, pacientes_all, path_grafica):
    q = []
    c = []
    for paciente in pacientes_all:
        comidas = pd.read_csv(root + paciente + '/food_dates_' + paciente + '.csv')
        comidas_filtrado = comidas[['quality', 'calories']]  # Taking a subset of columns
        # print(tabulate(comidas_filtrado, headers='keys', tablefmt='psql'))
        for index, row in comidas.iterrows():
            q.append(row["quality"])
        for index, row in comidas.iterrows():
            c.append(row["calories"])
    print(q)
    print(c)
    sns.set_theme(style="ticks", color_codes=True)
    ax = sns.catplot(x=q, y=c, data=comidas, kind='swarm', order=["Low quality", "Medium quality", "Good quality"])

    plt.title('Patients 1 to 9 Food calorie vs quality')
    plt.xlabel('Food quality')
    plt.ylabel('Calories (cal)')
    # leg = ax.legend()

    plt.show()

    plt.savefig(path_grafica)


