def viz_mnist_embedding(tensor, images, labels):
  '''Takes in a TF variable tensor, along with images and their 
     corresponding labels and sets up the projector to 
     visualize the data space.'''
  
  tb_dir = '/tmp/tflearn_logs'
  sess = tf.Session()
  sess.run(tensor.initializer)
  summary_writer = tf.summary.FileWriter(tb_dir)
  config = projector.ProjectorConfig()
  embedding = config.embeddings.add()
  embedding.tensor_name = tensor.name
  embedding.metadata_path = os.path.join(tb_dir, 'metadata.tsv')
  embedding.sprite.image_path = os.path.join(tb_dir, 'mnistdigits.png') 
  embedding.sprite.single_image_dim.extend([28,28])
  projector.visualize_embeddings(summary_writer, config)
  saver = tf.train.Saver([tensor])
  saver.save(sess, os.path.join(tb_dir, 'mnist_fc.ckpt'), 1)
  
  image_grid = montage(images, True)
  plt.imsave(os.path.join(tb_dir, 'mnistdigits.png'), image_grid, cmap='gray')
  
  with open(os.path.join(tb_dir, 'metadata.tsv'),'w') as f:
    f.write("Index\tLabel\n")
    for index,label in enumerate(labels):
      f.write("%d\t%d\n" % (index,label))
  f.close()
