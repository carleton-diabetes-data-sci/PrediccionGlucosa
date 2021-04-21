# casos

There are several files and folders:

* main.py : execution of main blocks of code

    * configuration : to define configutation. Paths and input paramenters

    * glucose_acceleration : for glucose and acceleration data processing

    * insulin : for insulin data processing

    * food : for food data processing
    
    * matrices : for matrices prepation 
    
    * execution : for the experiments training, validation and test.
    
    
# Error
    C:\Users\apula\PycharmProjects\PrediccionGlucosa\casos\matrices\separation.py:42: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
  df = pd.DataFrame(np.array(dimension_x_y_list), columns=['x', 'y', 'xTrain', 'yTrain', 'xVal', 'yVal', 'xTest', 'yTest'])
----SEPARATION: DIVIDE DATE INTO TRY CONFIGURATIONS
----SEPARATION: DIVIDE DATE INTO TRY CONFIGURATIONS
	 EJECUCION:  0
-- MODELS_TRIES: bloque_guardar_modelos_experimentos
-MODEL: SAVE MODEL OF A TRY AND PATIENT
2021-04-21 09:26:54.708416: I tensorflow/compiler/jit/xla_cpu_device.cc:41] Not creating XLA devices, tf_xla_enable_xla_devices not set
2021-04-21 09:26:54.709590: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library nvcuda.dll
2021-04-21 09:26:54.711699: E tensorflow/stream_executor/cuda/cuda_driver.cc:328] failed call to cuInit: CUDA_ERROR_UNKNOWN: unknown error
2021-04-21 09:26:54.715459: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: LAPTOP-47C244DH
2021-04-21 09:26:54.715622: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: LAPTOP-47C244DH
2021-04-21 09:26:54.715967: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2021-04-21 09:26:54.716540: I tensorflow/compiler/jit/xla_gpu_device.cc:99] Not creating XLA devices, tf_xla_enable_xla_devices not set
2021-04-21 09:26:54.991133: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:116] None of the MLIR optimization passes are enabled (registered 2)

SUMMARY

2021-04-21 09:27:12.326771: W tensorflow/python/util/util.cc:348] Sets are not currently considered sequences, but this may change in the future, so consider avoiding using them.
WARNING:absl:Found untraced functions such as lstm_cell_layer_call_fn, lstm_cell_layer_call_and_return_conditional_losses, lstm_cell_layer_call_fn, lstm_cell_layer_call_and_return_conditional_losses, lstm_cell_layer_call_and_return_conditional_losses while saving (showing 5 of 5). These functions will not be directly callable after loading.
WARNING:absl:Found untraced functions such as lstm_cell_layer_call_fn, lstm_cell_layer_call_and_return_conditional_losses, lstm_cell_layer_call_fn, lstm_cell_layer_call_and_return_conditional_losses, lstm_cell_layer_call_and_return_conditional_losses while saving (showing 5 of 5). These functions will not be directly callable after loading.
