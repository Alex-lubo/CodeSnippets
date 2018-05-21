# coding:utf-8

import tensorflow as tf

W = tf.Variable(tf.zeros([2, 1]), name='weights')
b = tf.Variable(0., name='bias')

def inference(X):
    return tf.matmul(X, W) + b

def loss(X, Y):
    # calculate the loss
    Y_ = inference(X)
    return tf.reduce_mean(tf.squared_difference(Y, Y_))
    # return tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(Y, Y_))

def inputs():
    X = []
    Y = []
    return tf.to_float(X), tf.to_float(Y)

def train(total_loss):
    learning_rate = 0.000001
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)

def evaluate(sess, tensor_X, tensor_Y):
    print sess.run(inference([[80., 25.]]))
    print sess.run(inference([[65., 25.]]))

saver = tf.train.Saver() # save traning date
writer = tf.summary.FileWriter('./supervised_graph', graph=tf.get_default_graph()) # save graphic

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    X, Y = inputs()
    total_loss = loss(X, Y)
    train_op = train(total_loss)
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    loss_summaries = tf.summary.scalar('loss_summaries', total_loss)
    # 实际的训练迭代次数
    training_step = 4000
    for step in range(training_step):
        sess.run([train_op])
        if step % 100 == 0:
            # 保存图
            writer.add_summary(sess.run(loss_summaries), global_step=step)
            print 'loss: ', sess.run(total_loss)
        if step % 1000 == 0:
            # 保存训练记录
            saver.save(sess, './my-model/regresion', global_step=step)

    # 评估
    evaluate(sess, X, Y)
    coord.request_stop()
    coord.join(threads)
    saver.save(sess, './my-model/regresion', global_step=training_step)
    writer.flush()
    writer.close()
    sess.close()
