

class Validator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("test call validator")
        print(kwargs)
        print(kwargs.items())

        for k, v in kwargs.items():
            print(k)
            # print(v)

            if type(v) == list:
                for vv in v:
                    print(vv)
            else:
                print(v)

            print("======")

        dict = {
            "domain_id": "required",
            "test": "string"
        }
        return {
            "dict": dict
        }



@Validator
def make(request):
    print(request)
    print("test make")



make(
    domain_id=["required", "string"],
    testing="required"
)
