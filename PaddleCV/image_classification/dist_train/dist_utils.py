import os
import paddle.fluid as fluid


def nccl2_prepare(args, startup_prog):
    config = fluid.DistributeTranspilerConfig()
    config.mode = "nccl2"
    t = fluid.DistributeTranspiler(config=config)

    envs = args.dist_env

    t.transpile(envs["trainer_id"],
        trainers=','.join(envs["trainer_endpoints"]),
        current_endpoint=envs["current_endpoint"],
        startup_program=startup_prog)


def pserver_prepare(args, train_prog, startup_prog):
    config = fluid.DistributeTranspilerConfig()
    config.slice_var_up = args.split_var
    t = fluid.DistributeTranspiler(config=config)
    envs = args.dist_env
    training_role = envs["training_role"]

    t.transpile(
        envs["trainer_id"],
        program=train_prog,
        pservers=envs["pserver_endpoints"],
        trainers=envs["num_trainers"],
        sync_mode=not args.async_mode,
        startup_program=startup_prog)
    if training_role == "PSERVER":
        pserver_program = t.get_pserver_program(envs["current_endpoint"])
        pserver_startup_program = t.get_startup_program(
            envs["current_endpoint"], pserver_program, startup_program=startup_prog)
        return pserver_program, pserver_startup_program
    elif training_role == "TRAINER":
        train_program = t.get_trainer_program()
        return train_program, startup_prog
    else:
        raise ValueError(
            'PADDLE_TRAINING_ROLE environment variable must be either TRAINER or PSERVER'
        )
