**1. В чём основное различие между unittest и pytest?**   
    Unittest является частью стандартной библиотеки Python, а его тесты проходят внутри класса. 
    Pytest необходимо устанавливать отдельно, но его тесты более компактные и содержатся в отдельных функциях.  
**2. Почему важно использовать автоматические тесты при разработке?**  
    Автоматические тесты позволяют находить ошибки на ранних этапах разработки, а также они повышают стабильность и ускоряют разработку, упрощая последующие модификации кода.  
**3. Какие есть виды ассертов в unittest и pytest?**  
    **В unittest:**  
    self.assertEqual(a, b)  
    self.assertNotEqual(a, b)  
    self.assertTrue(x)  
    self.assertFalse(x)  
    self.assertIsNone(x)    
    self.assertIn(a, b)  
    self.assertRaises(ErrorType, func, *args)    
    **В pytest:**  
    assert a == b  
    assert x is True  
    assert item in list  
    with pytest.raises(ErrorType): func()  
**4. Что делает @pytest.mark.parametrize?**  
  @pytest.mark.parametrize позволяет запустить один тест с разными входными данными:
```
@pytest.mark.parametrize("input, expected", [  
    (2, 4),
    (3, 9),
    (0, 0),  
])  
def test_square(input, expected):  
    assert input ** 2 == expected
```
**5. В каких случаях вы бы предпочли использовать pytest вместо unittest?**  
Я бы предпочел использовать pytest вместо unittest в тех случаях, когда код слишком масштабный, используются сторонние библиотеки или нужна маркеризация и параметризация.