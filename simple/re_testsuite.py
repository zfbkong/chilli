#Author:xiaoai
#Time:2020/4/9 5:04 PM
import unittest
# 构造测试集
def suite():
    # 实例化测试套件
    suite = unittest.TestSuite()
    # 将测试用例加载到测试套件中（执行顺序按照加载顺序执行）
    suite.addTest("test1")
    suite.addTest("test2")
    # 执行测试用例
    # 实例化TextTestRunner
    runner = unittest.TextTestRunner()
    # 使用run（）方法运行测试套件中的所有测试用例
    runner.run(suite)

# 执行用例的方案一
if __name__ =='__main__':
    unittest.main()
    suite()