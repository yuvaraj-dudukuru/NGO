import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Contact() {
    const navigate = useNavigate();

    // Controlled form state — React owns every input value
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });

    // Error state — drives inline validation messages
    const [errors, setErrors] = useState({});
    const [submitted, setSubmitted] = useState(false);

    // Single handler for all inputs using computed property names
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
        // Clear the error for this field as the user types
        if (errors[name]) {
            setErrors(prev => ({ ...prev, [name]: '' }));
        }
    };

    // Validation logic — runs before submission
    const validate = () => {
        const newErrors = {};
        if (!formData.name.trim()) newErrors.name = 'Name is required.';
        if (!formData.email.includes('@')) newErrors.email = 'Enter a valid email.';
        if (formData.message.length < 10) newErrors.message = 'Message must be at least 10 characters.';
        return newErrors;
    };

    const handleSubmit = (e) => {
        e.preventDefault(); // Critical: stops browser reload

        const validationErrors = validate();
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors); // Show errors, do NOT submit
            return;
        }

        // Simulate successful submission
        console.log('Form Submitted:', formData);
        setSubmitted(true);

        // Programmatic navigation: redirect to Home after 2 seconds
        setTimeout(() => navigate('/'), 2000);
    };

    const inputStyle = {
        width: '100%', padding: '12px', marginTop: '6px',
        backgroundColor: '#112240', border: '1px solid #233554',
        borderRadius: '6px', color: '#ccd6f6', fontSize: '15px',
        boxSizing: 'border-box'
    };

    const errorStyle = { color: '#ff6b6b', fontSize: '13px', marginTop: '4px' };

    if (submitted) {
        return (
            <div style={{ padding: '60px', textAlign: 'center', color: '#64ffda' }}>
                <h2>✅ Message Sent Successfully!</h2>
                <p style={{ color: '#a8b2d8' }}>Redirecting you to Home...</p>
            </div>
        );
    }

    return (
        <div style={{ padding: '60px', maxWidth: '560px', margin: '0 auto', color: '#ccd6f6' }}>
            <h1 style={{ color: '#64ffda', marginBottom: '30px' }}>Contact Us</h1>
            <form onSubmit={handleSubmit} noValidate>

                <div style={{ marginBottom: '20px' }}>
                    <label>Full Name</label>
                    <input
                        style={inputStyle} type="text"
                        name="name" value={formData.name}
                        onChange={handleChange} placeholder="Your name"
                    />
                    {errors.name && <p style={errorStyle}>{errors.name}</p>}
                </div>

                <div style={{ marginBottom: '20px' }}>
                    <label>Email Address</label>
                    <input
                        style={inputStyle} type="email"
                        name="email" value={formData.email}
                        onChange={handleChange} placeholder="you@example.com"
                    />
                    {errors.email && <p style={errorStyle}>{errors.email}</p>}
                </div>

                <div style={{ marginBottom: '20px' }}>
                    <label>Message</label>
                    <textarea
                        style={{ ...inputStyle, height: '120px', resize: 'vertical' }}
                        name="message" value={formData.message}
                        onChange={handleChange} placeholder="Write your message here..."
                    />
                    {errors.message && <p style={errorStyle}>{errors.message}</p>}
                </div>

                <button type="submit" style={{
                    width: '100%', padding: '14px', backgroundColor: '#64ffda',
                    color: '#0a192f', fontWeight: 'bold', fontSize: '16px',
                    border: 'none', borderRadius: '6px', cursor: 'pointer'
                }}>
                    Send Message
                </button>
            </form>
        </div>
    );
}

export default Contact;